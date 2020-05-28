Sites2 = mobility[bindingSelection]
print(Sites2)
print(np.mean(Sites2))
print(np.std(Sites2))
Sites1 = mobility[closeButNotBindingSite.astype(int)]
print(Sites1)
print(np.mean(Sites1))
print(np.std(Sites1))
