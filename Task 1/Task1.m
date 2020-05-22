%% Read the Audio
[x, fs] = audioread("audio1.wav");

%% Get y in time domain and add the Echo
y_t = zeros(length(x), 1);

for i = 1:length(x)
    y_t(i) = x(i);
    
    if i >= 2501
        y_t(i) = y_t(i) + x(i - 2500) * .9;
    end
    
    if i >= 4991
        y_t(i) = y_t(i) + x(i - 4990) * .8;
    end
    
    if i >= 7486
        y_t(i) = y_t(i) + x(i - 7485) * .7;
    end

end
sound(y_t); % the audio with echo

%% Get the impulse response

imp = zeros(length(x), 1);
imp(1) = 1;

h = imp;

for i = 1 : length(h)
    h(i, 1) = imp(i, 1);
    
    if i >= 2501
        h(i) = h(i) + imp(i - 2500) * .9;
    end
    
    if i >= 4991
        h(i) = h(i) + imp(i - 4990) * .8;
    end
    
    if i >= 7486
        h(i) = h(i) + imp(i - 7485) * .7;
    end
end

plot(h);
title('Impulse response');

%% Get y using convolution

y = conv(x, h);

%% Remove the echo using DFT

Y = fft(y);
H = fft(h);

H = imresize(H, [length(Y), 1]);

X = Y ./ H;

original_x = real(ifft(X));
sound(original_x(1: length(original_x) / 2));
