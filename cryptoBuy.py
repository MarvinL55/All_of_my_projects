import cbpro

public_client = cbpro.PublicClient()

results = public_client.get_products()

for row in results:
    print(row['id'])