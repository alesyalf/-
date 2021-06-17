from rewording import Tree, Node

tree = Tree('Новая схема')
tree.add_node(Node('Даю $апельсины и яблоки$ другу', 'картошка и морковь'))
tree.add_node(Node('Смотрю с утра $новости$', 'фильм'))
tree.add_node(Node('Перейти к  $Предоставлению со стороны субъектов отчетности о выбросах ПГ$',
                    'Оценка альтернатив блоков ЖЦ ВЭС'))
tree.children[0].add_child(Node('$Составление перечней альтернативных процессов ЖЦ ВЭС и их описаний$',
                                'Формированиями требований к итоговым процессам ЖЦ ВЭС от потребляющих их выход процессов'))
tree.change_all()
tree.print_all_nodes()

tree.delete_child(1)
tree.children[0].delete_child(0)
tree.print_all_nodes()