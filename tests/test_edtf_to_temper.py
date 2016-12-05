import pytest

from edtf_convert import edtf_to_temper


@pytest.mark.parametrize('edtf_date,temper_date', [
    ('2016-01-11', '20160111'),
    ('2012-04-12~', '20120412~'),
    ('2012-04-12?', '20120412?'),
    ('2008', '2008'),
    ('2004-11', '20041100'),
    ('(2011)-06-04~', '(:unav) unavailable'),
    ('[1667,1668,1670..1672]', '1667, 1668, 1670-1672'),
    ('[..1760-12-03]', '(:unav) unavailable'),
    ('{1902-01-16..1906-10-01}', '19020116-19061001'),
    ('[1975-08-07..1975-08-10]', '19750807-19750810'),
    ('1964/2008', '1964-2008'),
    ('2004-06/2006-08', '20040600-20060800'),
    ('[1923, 1924-09-01, 1925]', '1923, 1924, 1925'),
    ('2004-02-01/2005-02-08', '20040201-20050208'),
    ('2004-02-01/2005-02', '20040201-20050200'),
    ('2004-02-01/2005', '20040201-2005'),
    ('2005/2006-02', '2005-20060200'),
    ('2004-06-01/unknown', '20040601-'),
    ('1936/OPEN', '1936-'),
    ('2004-01-01/open', '20040101-'),
    ('1984~/2004-06', '1984~-20040600'),
    ('1984/2004-06~', '1984-20040600~'),
    ('1984?/2004?~', '1984?-2004?~'),
    ('2001-21', '2001'),
    ('1891, October 12', '(:unav) unavailable'),
    ('unknown', '(:unkn) unknown'),
    ('unknown/2006', '(:unav) unavailable'),
    ('2004-01-01/unknown', '20040101-'),
    ('[-0174..-0132]', '-0174--0132'),
])
def test_edtf_to_temper(edtf_date, temper_date):
    assert edtf_to_temper.EDTFToTEMPER(edtf_date).temper == temper_date
