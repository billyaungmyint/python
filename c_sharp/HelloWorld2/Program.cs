namespace HelloWorld2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] array1 = new int[3];
            array1[0] = 1;
            array1[1] = 2;
            array1[2] = 3;

            for (int i = 0; i < array1.Length; i++)
            {
                Console.WriteLine(i);
            }
        }
    }
}