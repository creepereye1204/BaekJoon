import java.util.*;
class tomato{
    int x;
    int y;
    int z;
    tomato(int x,int y,int z){
        this.x=x;
        this.y=y;
        this.z=z;
    }
}
class Main{
    public static int result=0;
    public static int[] dx={0,0,0,0,1,-1};
    public static int[] dy={0,0,1,-1,0,0};
    public static int[] dz={1,-1,0,0,0,0};

    public static Queue<tomato> queue = new LinkedList<>();
    public  static void travel(){
        for(int i=0;i<h;i++){
            for(int j=0;j<n;j++){
                for(int l=0;l<m;l++){
                    if(maps[i][j][l]==0){
                        System.out.println(-1);
                        System.exit(0);
                    }
                    if(result<maps[i][j][l]){
                        result=maps[i][j][l];
                    }

                }
            }
        }
    }
    public static void bfs(){
        while (!queue.isEmpty()){

                tomato t=queue.remove();
                int x=t.x;
                int y=t.y;
                int z=t.z;

                for(int i=0;i<6;i++){
                    if(-1<x+dx[i] && -1<y+dy[i] && -1<z+dz[i] && x+dx[i] <m &&  y+dy[i]<n && z+dz[i]<h && 0==maps[z+dz[i]][y+dy[i]][x+dx[i]]){

                        maps[z+dz[i]][y+dy[i]][x+dx[i]]=maps[z][y][x]+1;
                        queue.add(new tomato(x+dx[i],y+dy[i],z+dz[i]));
                    }
                }

        }

    }
    public static boolean freepass=true;
    public static int m;
    public static int n;
    public static int h;
    public static int[][][] maps;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);


        m = sc.nextInt();
        n = sc.nextInt();
        h = sc.nextInt();

        maps = new int[h][n][m];
        for(int i=0;i<h;i++){
            for(int j=0;j<n;j++){
                for(int l=0;l<m;l++){
                    maps[i][j][l]=sc.nextInt();
                    if(maps[i][j][l]==1){
                        queue.add(new tomato(l,j,i));
                    }
                    if(maps[i][j][l]==0){
                        freepass=false;
                    }
                }

            }
        }
        if(freepass){
            System.out.println(0);
        }
        else {
            bfs();
            travel();
            System.out.println(result-1);
        }
    }
}