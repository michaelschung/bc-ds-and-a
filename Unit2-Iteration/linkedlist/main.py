from linkedlist import LinkedList

def main():
    ll = LinkedList()
    ll.insert(5, 0)
    ll.insert(8, 1)
    ll.insert(56, 1)
    ll.print()
    print(ll.index(5))

if __name__ == '__main__':
    main()
