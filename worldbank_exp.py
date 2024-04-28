import wbgapi as wb
df = wb.data.DataFrame('NY.GDP.PCAP.CD', wb.region.members('EAP'), time=range(1980, 2020, 5), labels=True)
df.head()