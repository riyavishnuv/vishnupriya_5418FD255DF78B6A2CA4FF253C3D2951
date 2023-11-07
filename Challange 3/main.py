def linearSearchProduct(productlist, targetproduct):
    indices = []
    for index, product in enumerate(productlist):
        indices.append(index)
    return indices

product = ['shoes', 'boot', 'losfer', 'shoes', 'sandal', 'shoes']
target = 'shoes'
result = linearSearchProduct(product, target)
print(result)

                