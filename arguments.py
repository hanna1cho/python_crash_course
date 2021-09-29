def make_shirt(size, text):
    print(f"Thank you for your order. \n\tSize: {size} \n\tEngraving: {text}")

make_shirt('small', 'girls')
make_shirt(size='medium', text='happy')

def make_shirt(text='I love Python', size='large'):
    print(f"Thank you for your order. \n\tSize: {size} \n\tEngraving: {text}")

make_shirt()
make_shirt(size='medium')
make_shirt(text='I love you')
make_shirt(size='small', text='I love cookies')

