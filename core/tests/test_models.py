import random
import string
import pytest

from core.models import Category, Product, Retail


@pytest.fixture
def category(db) -> Category:
    return Category.objects.create(name="Books")


@pytest.fixture
def retailer_abc(db):
    return Retail.objects.create(name="ABC")


@pytest.fixture
def product_factory(db, category, retailer_abc):
    def create_product(name, description="A Book", mrp=None, is_available=True, retailers=None):
        if retailers is None:
            retailers = []
        sku = "".join(random.choices(string.ascii_uppercase +
                                     string.digits, k=6))
        product = Product.objects.create(
            sku=sku,
            name=name,
            description=description,
            mrp=mrp,
            is_available=is_available,
            category=category,
        )
        product.retails.add(retailer_abc)
        if retailers:
            product.retails.set(retailers)
        return product

    return create_product


@pytest.fixture
def product_one(product_factory):
    return product_factory(name="Book 1", mrp="100.2")


@pytest.fixture
def product_two(product_factory):
    return product_factory(name="Novel Book", mrp="51")


def test_product_retailer(db, retailer_abc, product_one):
    assert product_one.retails.filter(name=retailer_abc.name).exists()


def test_product_one(product_one):
    assert product_one.name == "Book 1"
    assert product_one.is_available

# @pytest.fixture
# def product_one(db, category):
#     return Product.objects.create(name="Book 1", category=category)


# @pytest.fixture
# def product_two(db, category):
#     return Product.objects.create(name="Book 2", category=category)


# def test_two_different_books_create(product_one, product_two):
#     assert product_one.pk != product_two.pk

# @pytest.fixture(params=("ABC123", "123456", "ABCDEF"))
# def product_one(db, request):
#     return Product.objects.create(name="Book 1", sku=request.param)


# def test_product_sku(product_one):
#     assert all(letter.isalnum() for letter in product_one.sku)
#     assert len(product_one.sku) == 6


# def test_filter_category(category):
#    assert Category.objects.filter(name="Books").exists()
#
#
# def test_update_category(category):
#    category.name = "DVDs"
#    category.save()
#    category_from_db = Category.objects.get(name="DVDs")
#    assert category_from_db.name == "DVDs"

# @pytest.fixture
# def category(db) -> Category:
#     return Category.objects.create(name="Books")


# @pytest.fixture
# def retailer_abc(db):
#     return Retail.objects.create(name="ABC")


# @pytest.fixture
# def retailers(db) -> list:
#     return []


# @pytest.fixture(autouse=True)
# def append_retailers(retailers, retailer_abc):
#     return retailers.append(retailer_abc)


# @pytest.fixture
# def product_one(db, category, retailers):
#     product = Product.objects.create(name="Book 1", category=category)
#     product.retails.set(retailers)
#     return product


# def test_product_retailer(db, retailer_abc, product_one):
#     assert product_one.retails.filter(name=retailer_abc.name).exists()
