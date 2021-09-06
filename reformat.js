var reformat = function(s) {
    const chars = [], nums = [];
    for (let i = 0; i < s.length; i++) {
        if (isNaN(+s[i])) {
            chars.push(s[i]);
        } else {
            nums.push(s[i]);
        }
    }
    if (Math.abs(chars.length - nums.length) > 1) return "";
    let longer = chars.length > nums.length ? chars : nums;
    let shorter = longer === chars ? nums : chars;
    let ans = "";
    while (shorter.length) {
        ans += longer.pop();
        ans += shorter.pop();
    }
    if (longer.length) ans += longer.pop();
    return ans;
};
