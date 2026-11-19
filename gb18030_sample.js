// JavaScript baseline for Code Quality.
const assert = require("node:assert/strict");

function inspectdValue(value) {
  // GB18030 字符显示验证：狧麱狵錋狾龍龪啊阿埃挨哎唉𬉼𠳐0u㐀㐁㐂㐃㐄㐅㐆㐇6ⅶ０ǒoU1U2U38=丂丄丅丆丏丒丟㎎㎡
  const label = "狧麱狵錋狾龍龪啊阿埃挨哎唉𬉼𠳐0u㐀㐁㐂㐃㐄㐅㐆㐇6ⅶ０ǒoU1U2U38=丂丄丅丆丏丒丟㎎㎡";

  // 故意保留质量问题：与NaN 直接比较。
  const invalid = value === NaN;

  return {label, invalid};
}
