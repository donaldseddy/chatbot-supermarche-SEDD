import { getAllProducts } from '@/services/productService';

export default async function ProductListPage() {
    const products = await getAllProducts();

    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-4">Liste des Produits</h1>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {products.map((product: any) => (
                    <div key={product._id} className="p-4 border rounded">
                        <h2 className="text-xl">{product.nom}</h2>
                        <p>{product.description}</p>
                        <p className="text-green-600">{product.prix} €</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
