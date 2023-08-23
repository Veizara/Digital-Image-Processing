function H = notch(type, M, N, D0, x, y, n)
if nargin == 6
   n = 1;
end
Hlp = lpfilter(type, M, N, D0, n);
H = 1 - Hlp;
H = circshift(H, [y-1 x-1]);
