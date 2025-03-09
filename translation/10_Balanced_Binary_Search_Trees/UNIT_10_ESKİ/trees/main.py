import datetime
import random
import time
import Tree


def main():
    # Write an XML file with the results
    file = open("AVL2SplayTree.xml", "w")

    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')

    file.write('<Plot title="AVL vs Splay Tree">\n')

    # Test size
    #number0fPoints = int(input("Enter the number of points : "))
    #values = []
    # Generate values
    xmin = 100
    xmax = 100000
    avl_time = []
    tree_size = []
    splay_time = []

    for i in range(xmin, xmax + 1, 1000):
        tree_size.append(i)
        # add random value
        values = [random.randint(0, i) for _ in range(i)]

        avl_tree = Tree.AVLTree()
        splay_tree = Tree.SplayTree()

        avl_type = []
        splay_type = []

        # for AVL tree
        unique_vals = [-1]
        time.sleep(1)
        starttime = datetime.datetime.now()
        for x in values:

            if x in unique_vals:


                avl_tree.lookup_value(x)
                endtime = datetime.datetime.now()
                avl_type.append("L")
            else:

                avl_tree.insert_value(x)
                avl_type.append("I")
                unique_vals.append(x)

        deltaTime = endtime - starttime
        accessTime = deltaTime.total_seconds() * len(avl_type)
        avl_time.append(accessTime)

        # for Splay tree

        unique_valsd = [-1]
        time.sleep(1)
        starttime = datetime.datetime.now()
        for x in values:

            if x in unique_valsd:
                n = Tree.Node(x)
                splay_tree.lookup(n, x)
                splay_type.append("L")
            else:


                splay_tree.insert(Tree.Node(x))
                splay_type.append("I")
                unique_valsd.append(x)

        endtime = datetime.datetime.now()
        deltaTime = endtime - starttime
        accessTime = deltaTime.total_seconds()*len(splay_type)
        splay_time.append(accessTime)

    file.write('  <Axes>\n')
    file.write('    <XAxis min="' + str(xmin) + '" max="' + str(xmax) + '"> Size</XAxis>\n')
    file.write('    <YAxis min="' + str(min(min(splay_time),min(avl_time))) + '" max="' + str(max(max(splay_time),max(avl_time))) + '">Microseconds</YAxis>\n')
    file.write('  </Axes>\n')

    file.write('  <Sequence title=" AVL tree points " color="red">\n')

    for i in range(len(avl_time)):
        file.write(
            '    <DataPoint  type="' + str(avl_type[i]) + '" x="' + str(tree_size[i]) + '" y="' + str(avl_time[i]) + '"/>\n')

    file.write('  </Sequence>\n')

    file.write('  <Sequence title=" Splay tree points " color="blue">\n')

    for i in range(len(splay_time)):
        file.write(
            '    <DataPoint type="' + str(splay_type[i]) + '" x="' + str(tree_size[i]) + '" y="' + str(splay_time[i]) + '"/>\n')

    file.write('  </Sequence>\n')
    file.write('</Plot>\n')
    file.close()


if __name__ == "__main__":
    main()
