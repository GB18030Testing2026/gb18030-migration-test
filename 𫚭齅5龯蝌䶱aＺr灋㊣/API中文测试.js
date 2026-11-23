function inspectValue(value) {
  // GB18030 字符验证：质量检查-𫠆𨐈繞繟繠繡繢繣繤魴龲龳亘兀丐廿卅丕亘鬲䦹䦺䦻䦼䦽䦾䦿䧀8b∨∑∏∪bU1U2U3怈怉怋怌怐怑怓怗㎝﹢⿻〇58b
  const label = "质量检查-𫠆𨐈繞繟繠繡繢繣繤魴龲龳亘兀丐廿卅丕亘鬲䦹䦺䦻䦼䦽䦾䦿䧀8b∨∑∏∪bU1U2U3怈怉怋怌怐怑怓怗㎝﹢⿻〇58b";
  const invalid = value === NaN;
  return { label, invalid };
}

console.log(inspectValue(Number("not-a-number")));
