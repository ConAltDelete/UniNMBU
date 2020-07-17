a = 5;

b = 10;

n = 100000;

h = (b-a) /n ;

y = h * sum( square(linspace(a+h/2,b-h/2,n-1)))

midpoint_rule(a,b,n)

function t = ro(a,b,n)
if a >= b
    t = b:1/n:a;
else
    t = a:1/n:b;
end
end
function f = square(x)
f = x .^ 2 + 1;
end
function Mf=midpoint_rule(a,b,N)

h=(b-a)/N;
%ci are your evaluation points
ci=linspace(a+h/2,b-h/2,N-1);
%This evaluates the function f, which is another matlab function
y=square(ci);
%you can just add up the vector y and multiply by h
Mf=h*sum(y);

end