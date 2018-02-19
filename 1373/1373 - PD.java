import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        int k;
        String[] x, y;

        k = Integer.parseInt(in.readLine());

        while (k > 0) {
            x = in.readLine().split("");
            y = in.readLine().split("");

            int tam_segmento;
            int n = x.length;
            int m = y.length;
            int[][] matriz = new int[n + 1][m + 1];

            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= m; ++j) {
                    tam_segmento = 0;
                    matriz[i][j] = Math.max(matriz[i-1][j], matriz[i][j-1]);

                    while(tam_segmento <= i-1 && tam_segmento <= j-1 && x[i-tam_segmento-1].equals(y[j-tam_segmento-1])) {
                        tam_segmento++;

                        if (tam_segmento >= k)
                            matriz[i][j] = Math.max(matriz[i][j], matriz[i-tam_segmento][j-tam_segmento]+tam_segmento);
                    }
                }
            }

            System.out.println(matriz[n][m]);

            k = Integer.parseInt(in.readLine());
        }
    }
}