from calories_tracker.macros import Macros

def test_macros_sum() -> None:
    m1 = Macros(10, 20, 5, 10)
    m2 = Macros(5, 3, 5, 10)

    total_macros = m1 + m2

    assert total_macros.calories == 15
    assert total_macros.carbs == 23
    assert total_macros.fats == 10
    assert total_macros.proteins == 20

def test_macros_scale() -> None:
    m1 = Macros(10, 20, 5, 10)
    m1.scale(50)

    m2 = Macros(10, 20, 5, 10)
    m2.scale(100)

    assert m1.calories == 5
    assert m1.carbs == 10
    assert m1.fats == 2.5
    assert m1.proteins == 5


    assert m2.calories == 10
    assert m2.carbs == 20
    assert m2.fats == 5
    assert m2.proteins == 10