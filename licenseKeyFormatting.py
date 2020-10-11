class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        q, rem = divmod(len(S), K)
        return "-".join(S[max(0, rem+K*(i-1)):rem+K*i] for i in range(q+1) if rem+K*i > 0)
