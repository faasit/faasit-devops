from faasit_runtime import function, create_handler, FaasitRuntime

from chameleon import PageTemplate

# import mmap
# lock_file = "lock"
# lock_string = "0"

# mm_lock = None
# with open(lock_file, 'rb') as f:
#     fd = f.fileno()
#     mm_lock = mmap.mmap(fd, 0, flags=mmap.MAP_SHARED, prot=mmap.PROT_READ)

# def wait():
#     while chr(mm_lock[0]) == lock_string:
#         pass

def get_timestamp():
    from datetime import datetime
    return str(datetime.now())

@function
def handle_func(frt:FaasitRuntime):
    wait()
    template = PageTemplate("""
    <html>
    <head>
        <title>${title} - Simple Web Application</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333366; }
            ul { background-color: #f0f0f0; padding: 20px; }
            li { color: #663333; }
            footer { font-size: 0.8em; color: #777777; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Welcome to ${title}!</h1>
        <p>Hello, ${user}! Thank you for visiting.</p>
        <ul>
            <li tal:repeat="item items">
                ${item}
            </li>
        </ul>
        <footer>
            <p>Last updated at: ${timestamp()}</p>
        </footer>
    </body>
    </html>
    """)
    rendered = template.render(title="Chameleon Page", user="Guest", items=['Item 1', 'Item 2', 'Item 3'], timestamp=get_timestamp)
    # print(rendered)
    return frt.output(rendered)

handler = create_handler(handle_func)