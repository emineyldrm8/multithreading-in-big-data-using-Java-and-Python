
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import javax.swing.table.DefaultTableModel;


public class WorkerThread extends Thread implements Runnable {

    private long baslangiczamani;
    private long calismasuresi;

    public long getBaslangiczamani() {
        return baslangiczamani;
    }

    public void setBaslangiczamani(long baslangiczamani) {
        this.baslangiczamani = baslangiczamani;
    }

    public long getCalismasuresi() {
        return calismasuresi;
    }

    public void setCalismasuresi(long calismasuresi) {
        this.calismasuresi = calismasuresi;
    }
// 3 main pagedeki durum için kodlar yazilacak
    public int findMatchCount(String[] a, String[] b) {
        List<String> list1 = new ArrayList(Arrays.asList(a));
        List<String> list2 = Arrays.asList(b);
        list1.retainAll(list2);
        return list1.size();
    }
   
 
    public float islemyaptir(String[] a, String[] b) {
        int kontrol = 0;
        if (a.length > b.length) {
            kontrol = 1;
        }

        if (a.length < b.length) {

            kontrol = -1;
        }
        if (a.length == b.length) {

            kontrol = 0;

        }

        float benzerlikorani = 0;
        if (kontrol == 1) {
            int sonuc2 = findMatchCount(a, b);

            //burada a buyuktur b oldugundan anın uzunlugu alınacak
            benzerlikorani = (((float) sonuc2) / ((float) a.length)) * 100;

        }
        if (kontrol == (-1)) {
            int sonuc2 = findMatchCount(a, b);
            //b uzun

            benzerlikorani = (((float) sonuc2) / ((float) b.length)) * 100;

        }
        if (kontrol == 0) {
            int sonuc2 = findMatchCount(a, b);

            benzerlikorani = (((float) sonuc2) / ((float) b.length)) * 100;
        }
        return benzerlikorani;
    }
      public int secim;

    public int getSecim() {
        return secim;
    }

    public void setSecim(int secim) {
        this.secim = secim;
    }
    public long kararfonksiyonu(int secim)
    {
        
        baslangiczamani=System.nanoTime();
      if(secim==1){
               benzerlikfiltre b1=new benzerlikfiltre();
              // b1.anafonksiyon();
              
               calismasuresi = System.nanoTime()-baslangiczamani;
               return calismasuresi;}
               
          if(secim==2){
                benzerlikarastirma b2=new benzerlikarastirma();
               // b2.anafonksiyon();
                 calismasuresi = System.nanoTime()-baslangiczamani;
                 return calismasuresi;}
        if(secim==3){
               sutunelemanarama b3=new sutunelemanarama();
              // b3.anafonksiyon();
               calismasuresi = System.nanoTime()-baslangiczamani;
               return calismasuresi;}
             return 0;} 
      
       
        
   
      //jbutton1 benzerlikfiltre
    public void run() {
     kararfonksiyonu(secim);
    } 
     
         
               

      
        
        
        
        
        
        
        
        
        
        
        
    
    
}
