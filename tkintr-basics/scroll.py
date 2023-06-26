from tkinter import *

root = Tk()
root.geometry("800x800")
root.title("Scroll")

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH, expand=True)

scrollbar.config(command=text.yview)

text.insert(END, "<p>Lorem ipsum dolor sit amet. Sit voluptas nesciunt aut pariatur sint et soluta veritatis! Eos repellendus possimus eos eaque voluptatibus ea sunt consequatur est animi possimus ex quas Quis. Aut dolores rerum et dolorum eaque quo modi voluptate qui excepturi natus qui doloremque harum. Est exercitationem rerum rem beatae accusamus nam beatae velit qui impedit dolor et commodi quia! </p><p>Aut rerum quia et consequatur impedit hic velit sunt est deserunt voluptas. Qui beatae velit id libero voluptatem sit quia consequatur quo quia animi est nobis galisum ab magni numquam sit sequi natus. </p><p>Et corrupti voluptatem est quasi sint id veritatis nihil non dicta optio. Sit ullam corporis et iure omnis ut voluptas voluptatibus aut cumque dolores ea exercitationem dignissimos qui aliquid officia. Est libero sapiente non voluptates voluptas qui dolorum dolor aut earum aspernatur ex illo optio ea aliquam dolor! Sit quibusdam dignissimos ut tempora accusantium eos enim obcaecati sed soluta officiis qui reprehenderit perferendis ut dolor libero! </p>")

root.mainloop()
