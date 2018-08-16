clearvars;

resfiles = {'~/Documents/work/wire_wrap/inf_original/inf_res.m', '~/Documents/work/wire_wrap/inf_wire/inf_res.m', '~/Documents/work/wire_wrap/inf_mod/inf_res.m', '~/Documents/work/wire_wrap/inf_mod2/inf_res.m', '~/Documents/work/wire_wrap/inf_pressure/inf_res.m', '~/Documents/work/wire_wrap/inf_temp/inf_res.m', '~/Documents/work/wire_wrap/inf_combined/inf_res.m'};
depfiles = {'~/Documents/work/wire_wrap/inf_original/inf_dep.m', '~/Documents/work/wire_wrap/inf_wire/inf_dep.m', '~/Documents/work/wire_wrap/inf_mod/inf_dep.m', '~/Documents/work/wire_wrap/inf_mod2/inf_dep.m', '~/Documents/work/wire_wrap/inf_pressure/inf_dep.m', '~/Documents/work/wire_wrap/inf_temp/inf_dep.m', '~/Documents/work/wire_wrap/inf_combined/inf_dep.m'};

figure;
for j = 1:length(resfiles)
    run(resfiles{j});
    run(depfiles{j});

    nHM = (MAT_fuel_ADENS(i922350,1) + MAT_fuel_ADENS(i922380,1))*MAT_fuel_VOLUME(1)*10^24; %assuming only HM isotopes are U235 and U238
    FIMA = zeros(1,idx); balance = zeros(1,idx);
    FIMA(1) = 0; balance(1) = 0;
    for i = 2:idx
        FIMA(i) = FIMA(i-1) + (TOT_FISSRATE(i-1,1)+TOT_FISSRATE(i,1))/2 * (BURN_DAYS(i)-BURN_DAYS(i-1))*24*60*60/nHM; %using the average of fission rates between steps
        balance(i) = balance(i-1) + nHM*( NUBAR(i,1)*(1 - 1/(ANA_KEFF(i,1))) + NUBAR(i-1,1)*(1 - 1/(ANA_KEFF(i-1,1))) )/2 * (FIMA(i) - FIMA(i-1)); %using the midpoint rule
    end

    plot(FIMA, balance);
    hold on;
    
    clearvars -except resfiles depfiles FIMA;
end

plot([0, FIMA(end)], [0 0], 'k--');
grid on; xlabel('FIMA'); ylabel('neutron balance');
legend('original', 'wire', 'mod', 'mod2', 'pressure', 'temp', 'combined');