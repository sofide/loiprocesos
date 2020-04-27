class OrderError(Exception):
    pass


def get_previous_and_next_ids(queryset):
    """Get previous and next ids for each element of a queryset.

    Given a queryset, return a list of tuples where the first element is an element
    from queryset, the second one is the id of the previous element and the third one is
    the id of the next element.

    For example:
    get_previous_and_next_ids(queryset(Elem 1, Elem 2, Elem3))
    >> [(Elem1, None, 2), (Elem2, 1, 3), (Elem3, 2, None)]
    """
    all_elements = list(queryset)
    first = 0
    last = len(queryset) -1

    elements_with_previous_and_next = []

    for i, element in enumerate(all_elements):
        if i == first:
            previous = None
        else:
            previous = all_elements[i-1].pk

        if i == last:
            next_element = None
        else:
            next_element = all_elements[i+1].pk

        elements_with_previous_and_next.append((element, previous, next_element))

    return elements_with_previous_and_next


def switch_order(element_1, element_2):
    """Switch 'orden' value between two elements if they are adjacent.

    Raise OrderError if the elements are not adjacent, or they are from different
    classes or units.
    """
    model_class, unidad = get_class_and_unit(element_1, element_2)

    if not are_adjacents(element_1, element_2):
        update_order(model_class, unidad)
        element_1 = model_class.objects.get(pk=element_1.pk)
        element_2 = model_class.objects.get(pk=element_2.pk)

        if not are_adjacents(element_1, element_2):
            msg = "Cannot switch order of {} and {} because they are not adjacent"
            raise OrderError(msg.format(element_1, element_2))

    orig_element_1_orden = element_1.orden
    orig_element_2_orden = element_2.orden

    element_1.orden = orig_element_2_orden
    element_2.orden = orig_element_1_orden

    element_1.save()
    element_2.save()


def are_adjacents(element_1, element_2):
    """Check if two elements are adjacents.

    Return True if the elements are next to each other
    """
    return abs(element_1.orden - element_2.orden) == 1


def get_class_and_unit(element_1, element_2):
    """Get class and unit from the received elements.

    Raise OrderError if the element are from different classes or units.
    """
    if element_1.__class__ != element_2.__class__:
        raise OrderError("{} and {} are from different classes.")

    if element_1.unidad != element_2.unidad:
        raise OrderError("{} and {} are from different units.")

    return element_1.__class__, element_1.unidad


def update_order(model, unidad):
    """
    Update de order of all elements of the given model and unit.
    """
    elements_to_order = model.objects.filter(unidad=unidad)

    for order, element in enumerate(elements_to_order):
        if element.orden != order:
            element.orden = order
            element.save()
