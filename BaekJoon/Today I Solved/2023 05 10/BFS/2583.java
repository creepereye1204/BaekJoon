import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Area {
    public static int q=1;
    public static int m;
    public static int n;
    public static int k;
    public static int[][] maps;
    public static int[] dx={0,0,1,-1};
    public static int[] dy={1,-1,0,0};

    public static void dfs(int x,int y){
        q++;
        maps[y][x]=1;
        for(int i=0;i<4;i++){
            int xx=x+dx[i];
            int yy=y+dy[i];
            if(-1<xx && -1 < yy && xx<n && yy<m && maps[yy][xx]==0){

                dfs(xx,yy);

            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        ArrayList<Integer> result= new ArrayList<>();

        maps= new int[m][n];
        for(int i=0;i<k;i++){
            st = new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            int c=Integer.parseInt(st.nextToken());
            int d=Integer.parseInt(st.nextToken());
            for(int y=b;y<d;y++){
                for(int x=a;x<c;x++){
                    maps[y][x]=1;
                }
            }

        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(maps[i][j]==0){
                    q=0;
                    dfs(j,i);
                    result.add(q);
                }
            }
        }
        Collections.sort(result);
        System.out.println(result.size());
        for(int i:result){
            System.out.print(i+" ");
        }

    }
}
