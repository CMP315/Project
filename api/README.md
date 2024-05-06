
# API

The back-end of the Password Manager.

## Run Locally
1. [Install Python](https://www.python.org/downloads/)
2. [Install Git](https://git-scm.com/downloads)
3. Clone the project
```bash
  git clone https://github.com/CMP315/API.git CMP315-API
```
4. Go to the project directory
```bash
  cd CMP315-API
```
5. [Create .env File](#example-env-file)
6. Install dependencies
```bash
  pip install -r requirements.txt
```
7. Start the server
```bash
  python src/main.py
```

## API Documentation
[View Here @ Postman.co](https://cmp315.postman.co/workspace/New-Team-Workspace~ef0c1772-3d09-4444-98f4-23cfd4ed276a/collection/17093352-9164dec6-91af-43f3-ba32-7b6c2867698f?action=share&creator=17093352)

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file

| NAME                   | TYPE    | DEFAULT VALUES                                                                                               |
|------------------------|---------|--------------------------------------------------------------------------------------------------------------|
| MONGODB_CONNECTION_URL | String  | `mongodb+srv://USERNAME:PASSWORD@cluster0.vz4azvs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0` |
| DEBUG                  | Boolean | `true`                                                                                                       |
| HTTPS                  | Boolean | `false`                                                                                                      |
| DATABASE_NAME          | String  | `cmp315-api`                                                                                                 |

### Example .env File
If you are following the installation steps above, you should put the `.env` file within the **CMP315-API** folder.
```env
DEBUG=true
HTTPS=false
MONGODB_CONNECTION_URL=mongodb+srv://cmp315:cmp315@cluster0.vz4azvs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
DATABASE_NAME=cmp315-api
```

## Usage/Examples

```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // Create an instance of HttpClient
        using (HttpClient client = new HttpClient())
        {
            try
            {
                // Call the API endpoint
                HttpResponseMessage response = await client.GetAsync("https://api.example.com/data");
                
                // Check if the response is successful
                if (response.IsSuccessStatusCode)
                {
                    // Read the response content as a string
                    string content = await response.Content.ReadAsStringAsync();
                    
                    // Output the response content
                    Console.WriteLine(content);
                }
                else
                {
                    Console.WriteLine($"Failed to call the API. Status code: {response.StatusCode}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
