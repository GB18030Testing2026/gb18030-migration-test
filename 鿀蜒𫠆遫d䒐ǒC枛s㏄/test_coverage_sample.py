import importlib.util
from pathlib import Path

source_path = Path(__file__).with_name("计算.py")
spec = importlib.util.spec_from_file_location("gb18030_coverage_module", source_path)

if spec is None or spec.loader is None:
    raise ImportError(f"Cannot load source module: {source_path}")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
describe_number = module.describe_number

def test_positive():
  assert describe_number(1) == "正数-舰剑饯渐溅建僵齄鿀龬ɑπ㈢Ｑ𫓧𬬮U1U2U3()ao㩹㩺㩻㩼㩽䀃E9;cz囌囍囎囐囓囑囒㏄㏑⿲⿳⿻〇cz珸珹䲟珺珻珼陫龫龭姜将浆江疆蒋丌𬴂𫘦琀琁琂琄琇琈琌8U^5䀆䀇䀈䀌䶫䶬U1U2U3Ⅷ４ξú+0-R囕囖囘並噝㏒╲﹫8U^5"

def test_zero():
  assert describe_number(0) == "非正数-舰剑饯渐溅建僵齄鿀龬ɑπ㈢Ｑ𫓧𬬮U1U2U3()ao㩹㩺㩻㩼㩽䀃E9;cz囌囍囎囐囓囑囒㏄㏑⿲⿳⿻〇cz珸珹䲟珺珻珼陫龫龭姜将浆江疆蒋丌𬴂𫘦琀琁琂琄琇琈琌8U^5䀆䀇䀈䀌䶫䶬U1U2U3Ⅷ４ξú+0-R囕囖囘並噝㏒╲﹫8U^5"
