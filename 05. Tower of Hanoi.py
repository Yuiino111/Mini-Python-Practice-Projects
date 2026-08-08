def hanoi_solver(n):
    A = list(range(n, 0 , -1))
    B = []
    C = []
    lines = []

    def record_state():
        lines.append(f"{A} {B} {C}")

    def move_disks(count, source, target, auxiliary):
        if count == 0:
            return
        
        move_disks(count-1, source, auxiliary, target)

        target.append(source.pop())
        record_state()

        move_disks(count-1, auxiliary, target, source)

    record_state()
    move_disks(n, A, C, B)

    return "\n".join(lines)

#Test
print (hanoi_solver(3))
