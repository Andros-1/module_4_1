import fake_math as f
import true_math as t

fake_divide = f.divide
true_divide = t.divide

res1 = fake_divide(69, 3)
res2 = fake_divide(3, 0)
res3 = true_divide(49, 7)
res4 = true_divide(15, 0)

print(res1)
print(res2)
print(res3)
print(res4)