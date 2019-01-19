import gdchart

import shelve

shelve_file  = shelve.open('access.s')

items_list = [(i[0],i[0]) for i in shelve_file.items()]

items_list.sort()
bytes_sent = [i[0] for i in tems_list]
# ip_addres = [(i[0],i[0]) for i in shelve_file.items()]

ip_addresses = ['xxx.xxx.xxx.xxx' for i in items_list]

chart = gdchart.Bar90

chart.width = 400
chart.height = 400
chart.gb_color = 'white'
chart.plot_color = 'black'
chart.xtitle = 'IP Address'
chart.setData(bytes_sent)
chart.setLabels(ip_addresses)
chart.draw("Bytes_ip_bar.png")
shelve.close()

