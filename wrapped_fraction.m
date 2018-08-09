nrings = 1:9;
npins = [1];

for i = nrings(2:end)
    tmp = 1;
    for j = 2:i
        tmp = tmp + (j-1)*6;
    end
    npins(end+1) = tmp;
end

nwraps_1 = [1];
for i = nrings(2:end)
    tmp = 0;
    for j = 2:i
        if (mod(j,2) == 0)
            tmp = tmp + (j-1)*6;
        else
            tmp = tmp + (j-1)*6/2;
        end
    end
    if mod(j,2) == 1
        tmp = tmp + (j-1)*6/2;
    end
    nwraps_1(end+1) = tmp;
end

F_1 = nwraps_1./npins;

nwraps_2 = [1 7 16 34 52 76 100 130 166]; %didn't calculate the last one

F_2 = nwraps_2./npins;

plot(nrings, F_1, nrings, F_2);
xlabel('number of rings'); ylabel('fraction of pins with wire wraps');
legend('center pin is not wrapped', 'center pin is wrapped'); grid on;