from src.Vector2D import Vector2D

def test_vector_addition():
    vector_a = Vector2D(2, 3)
    vector_b = Vector2D(4, 1)

    result_vector = vector_a + vector_b

    assert result_vector.x == 6
    assert result_vector.y == 4

def test_vector_subtraction():
    vector_a = Vector2D(2, 3)
    vector_b = Vector2D(4, 1)

    result_vector = vector_a - vector_b
    
    assert result_vector.x == -2
    assert result_vector.y == 2

def test_vector_multiplication():
    vector_a = Vector2D(2, 3)
    scalar = 3

    result_vector = vector_a * scalar
    
    assert result_vector.x == 6
    assert result_vector.y == 9

def test_vector_magnitude():
    vector_a = Vector2D(4, 3)

    magnitude = vector_a.magnitude()
    
    assert magnitude == 5

def test_vector_normalization():
    vector_a = Vector2D(4, 3)

    result_vector = vector_a.normalization()
    
    assert result_vector.x == 0.8
    assert result_vector.y == 0.6

def test_vector_normalization_zero_division():
    vector_a = Vector2D(0, 0)

    result_vector = vector_a.normalization()
    
    assert result_vector.x == 0
    assert result_vector.y == 0