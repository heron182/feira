import pytest
from django.urls import reverse
from model_mommy import mommy

from api.models import Bairro, Distrito, Feira, Regiao, SubPrefeitura, SubRegiao
from api.serializers import FeiraSerializer


@pytest.mark.django_db
def test_list_distritos(api_client):
    mommy.make(Distrito, _quantity=10)
    resp = api_client.get(reverse("distrito-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_distrito_by_id(api_client):
    distrito = mommy.make(Distrito)
    resp = api_client.get(reverse("distrito-detail", args=([distrito.id])))

    assert resp.status_code == 200
    assert resp.json()["id"] == distrito.id


@pytest.mark.django_db
def test_list_sub_prefeituras(api_client):
    mommy.make(SubPrefeitura, _quantity=10)
    resp = api_client.get(reverse("sub-prefeitura-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_sub_prefeitura_by_id(api_client):
    sub_prefeitura = mommy.make(SubPrefeitura)
    resp = api_client.get(reverse("sub-prefeitura-detail", args=([sub_prefeitura.id])))

    assert resp.status_code == 200
    assert resp.json()["id"] == sub_prefeitura.id


@pytest.mark.django_db
def test_list_regioes(api_client):
    mommy.make(Regiao, _quantity=10)
    resp = api_client.get(reverse("regiao-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_regiao_by_id(api_client):
    regiao = mommy.make(Regiao)
    resp = api_client.get(reverse("regiao-detail", args=([regiao.id])))

    assert resp.status_code == 200
    assert resp.json()["id"] == regiao.id


@pytest.mark.django_db
def test_list_sub_regioes(api_client):
    mommy.make(SubRegiao, _quantity=10)
    resp = api_client.get(reverse("sub-regiao-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_sub_regiao_by_id(api_client):
    sub_regiao = mommy.make(SubRegiao)
    resp = api_client.get(reverse("sub-regiao-detail", args=([sub_regiao.id])))

    assert resp.status_code == 200
    assert resp.json()["id"] == sub_regiao.id


@pytest.mark.django_db
def test_list_bairros(api_client):
    mommy.make(Bairro, _quantity=10)
    resp = api_client.get(reverse("bairro-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_bairro_by_id(api_client):
    bairro = mommy.make(Bairro)
    resp = api_client.get(reverse("bairro-detail", args=([bairro.id])))

    assert resp.status_code == 200
    assert resp.json()["id"] == bairro.id


@pytest.mark.django_db
def test_list_feiras(api_client):
    mommy.make(Feira, _quantity=10)
    resp = api_client.get(reverse("feira-list"))

    assert resp.status_code == 200
    assert len(resp.json()["results"]) == 10


@pytest.mark.django_db
def test_get_feira_by_id(api_client):
    feira = mommy.make(Feira)
    resp = api_client.get(reverse("feira-detail", args=([feira.id])))

    assert resp.status_code == 200
    assert resp.json()["id"] == feira.id


@pytest.mark.django_db
def test_create_feira(api_client):
    feira = mommy.prepare(Feira, _save_related=True)
    data = dict(
        nome=feira.nome,
        lat=feira.lat,
        long=feira.long,
        registro=feira.registro,
        areap=feira.areap,
        setcens=feira.setcens,
        logradouro=feira.logradouro,
        numero=feira.numero,
        referencia=feira.referencia,
        distrito_id=feira.distrito_id,
        sub_pref_id=feira.sub_pref_id,
        sub_regiao_id=feira.sub_regiao_id,
        bairro_id=feira.bairro_id,
    )
    resp = api_client.post(reverse("feira-list"), data=data, format="json")

    assert resp.status_code == 201
    assert Feira.objects.get(registro=data["registro"])


@pytest.mark.django_db
def test_patch_feira(api_client):
    feira = mommy.make(Feira)
    data = {"nome": "Feira do Carlos Blanka"}
    resp = api_client.patch(reverse("feira-detail", args=([feira.id])), data=data)

    import ipdb

    ipdb.set_trace()
    assert resp.status_code == 200
    assert resp.json()["nome"] == data["nome"]


@pytest.mark.django_db
def test_cannot_patch_feira_registro(api_client):
    feira = mommy.make(Feira)
    data = {"nome": "Feira do Carlos Blanka", "registro": "8979"}
    resp = api_client.patch(reverse("feira-detail", args=([feira.id])), data=data)

    assert resp.status_code == 400
    assert resp.json() == {"detail": "Cannot patch registro field"}
