## 快速地址转换TLB

* 问题由来：分页逻辑上需要一次额外的内存访问。每次指令获取、显式加载或保存，都要额外读一次内存以得到转换信息。

* 地址转换缓冲：地址转换旁路缓冲存储器（translation-lookasidebuffer，TLB[CG68,C95]），
它就是频繁发生的虚拟到物理地址转换的硬件缓存（cache）。因此，更好的名称应该是地址转换缓存（address-translation cache）。
对每次内存访问，硬件先检查TLB，看看其中是否有期望的转换映射,虚拟页号到页表项的映射。
```
VPN = (VirtualAddress & VPN_MASK) >> SHIFT
(Success, TlbEntry) = TLB_Lookup(VPN)
if (Success == True) // TLB Hit
    if (CanAccess(TlbEntry.ProtectBits) == True)
        Offset = VirtualAddress & OFFSET_MASK
        PhysAddr = (TlbEntry.PFN << SHIFT) | Offset
        AccessMemory(PhysAddr)
    else
        RaiseException(PROTECTION_FAULT)
else // TLB Miss
    PTEAddr = PTBR + (VPN * sizeof(PTE))
    PTE = AccessMemory(PTEAddr)
    if (PTE.Valid == False)
        RaiseException(SEGMENTATION_FAULT)
    else if (CanAccess(PTE.ProtectBits) == False)
        RaiseException(PROTECTION_FAULT)
    else
        TLB_Insert(VPN, PTE.PFN, PTE.ProtectBits)
        RetryInstruction()
TLB 处理器核心附近，设计的访问速度很快。如果TLB未命中，就会带来很大的分页开销。必须访问页表来查找转换映射，
导致一次额外的内存引用。
```     

* TLB的内容：一条TLB 项内容可能像下这样：VPN ｜ PFN ｜ 其他位。
``` 
TLB 的有效位!=页表的有效位
    如果一个页表项（PTE）被标记为无效，就意味着该页并没有被进程申请使用，正常运行的程序不应该访问该地址。
    TLB 的有效位不同，只是指出TLB 项是不是有效的地址映射，没有地址转换映射被缓存在这里。
``` 

* 上下文切换时对TLB 的处理：
    * 方案1：在上下文切换时，简单地清空（flush）TLB，这样在新进程运行前TLB 就变成了空的。但是，有一定开销：每次进程运行，当它访问数据和代码页时，都会触发TLB未命
中。如果操作系统频繁地切换进程，这种开销会很高。

    * 方案2：系统增加了硬件支持，实现跨上下文切换的TLB 共享。比如有的系统在TLB 中添加了一个地址空间标识符（Address Space Identifier，ASID），实现了跨进程的TLB共享。

   
        
        