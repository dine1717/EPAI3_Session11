
from session11_1 import RegularPoly
from session11_2 import RegularPolySeq
import os
import inspect
import re
import math
import pytest


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = RegularPoly(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = RegularPoly(n, R)
    
    assert p.vert_count == n, (f'actual: {p.vert_count},'
                                   f' expected: {n}')
    assert p.edge_count == n, f'actual: {p.edge_count}, expected: {n}'
    assert p.radius == R, f'actual: {p.radius}, expected: {n}'
    assert p.interior_angle == 57.29577951308232, (f'actual: {p.interior_angle},'
                                    ' expected: 57.29577951308232')
    n = 4
    R = 1
    p = RegularPoly(n, R)
    assert p.interior_angle == 114.59155902616465, (f'actual: {p.interior_angle}, '
                                    ' expected: 114.59155902616465')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.edge_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    p = RegularPoly(6, 2)
    assert math.isclose(p.edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    # assert math.isclose(p.interior_angle, 230,
    #                     rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = RegularPoly(12, 3)
    assert math.isclose(p.edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    # assert math.isclose(p.interior_angle, 150,
    #                     rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = RegularPoly(3, 10)
    p2 = RegularPoly(10, 10)
    p3 = RegularPoly(15, 10)
    p4 = RegularPoly(15, 100)
    p5 = RegularPoly(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


def test_count_vertices():
    p = RegularPoly(4,4)
    assert p.vert_count == 4,'did not match'

def test_count_edges():
    p = RegularPoly(4,4)
    assert p.edge_count == 4,'did not match'

def test_radius():
    p = RegularPoly(4,4)
    assert p.radius == 4,'did not match'

def test_interior_angle():
    p = RegularPoly(3,1)
    assert p.interior_angle == 57.29577951308232,'did not match'

def test_edge_length():
    p = RegularPoly(7,10)
    assert p.edge_length == 8.677674782351163,'did not match'

def test_apothem():
    p = RegularPoly(7,10)
    assert p.apothem == 9.009688679024192,'did not match'

def test_area():
    p = RegularPoly(7,10)
    assert p.area == 273.6410188638105,'did not match'

def test_perimeter():
    p = RegularPoly(7,10)
    assert p.perimeter == 60.74372347645814,'did not match'

def test_polygons_len():
    pp = RegularPolySeq(7,10)
    assert pp.__len__() == 5,'length did not match'

def test_iterator():
    polygons = RegularPolySeq(6, 10)
    iter_poly = iter(polygons)
    assert str(next(iter_poly)) == '(RegularPoly(3, 10), 2.5000000000000004)', "Please check yout implementation"
    assert str(next(iter_poly)) == '(RegularPoly(4, 10), 3.5355339059327378)', "Please check yout implementation"
    assert str(next(iter_poly)) == '(RegularPoly(5, 10), 4.045084971874737)', "Please check yout implementation"
    assert str(next(iter_poly)) == '(RegularPoly(6, 10), 4.330127018922194)', "Please check yout implementation"
    with pytest.raises(StopIteration):
        next(iter_poly)
    print("Polygons Class has implemented iterator functionality")


def test_iteratorfunc():
    polygons = RegularPolySeq(6, 10)    
    assert hasattr(polygons.PolygonIterator, '__iter__'), "Please check yout implementation"
    assert hasattr(polygons.PolygonIterator, '__next__'), "Please check yout implementation"
    assert callable(polygons.PolygonIterator.__iter__), "Please check yout implementation"    
    assert hasattr(polygons,'__getitem__'), "Please check yout implementation"
    assert callable(polygons.__getitem__), "Please check yout implementation"
    print("polygon object has all required attributes and functionality")


def test_iterable():
    polygons = RegularPolySeq(5, 10)
    iter_poly = iter(polygons)
    assert "iterator" in str(iter_poly), "Please check yout implementation"
    assert iter_poly.__next__(), "Please check yout implementation"
    print("Iterable functionality is working fine, next() is implemented")

def test_listable():
    polygons = RegularPolySeq(10, 10)
    assert len(list(polygons)) == 8, "Please check yout implementation"
    #assert str([1]) == "Polygon(n=4, R=10)", "Please check yout implementation"
    #assert str(polygons[2]) == "Polygon(n=5, R=10)", "Please check yout implementation"
    print("Giving apt output when called as list(polygons)")  

def test_iterables_exhaust():
    polygons = RegularPolySeq(4, 10)
    polygons_list = []
    for poly in polygons:
        polygons_list.append(poly)
        print(poly)
    for poly in polygons:
        polygons_list.append(poly)
        print(poly)
    assert len(polygons_list) > len(list(polygons)), "Please check yout implementation"
    assert len(polygons_list) == 4, "Please check yout implementation"
    print("For loop was done over polygon twice and it didnt get exhaust")