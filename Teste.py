
import os 

os.environ['ACCOUNT_SID'] = 'ACc906b1cb84d639c680889d5ab72f36d1'
os.environ['AUTH_TOKEN'] = 'd17207df74ca9a0514acb12eb422ded0'

print(os.environ.get('ACCOUNT_SID'))
print(os.environ.get('AUTH_TOKEN'))
