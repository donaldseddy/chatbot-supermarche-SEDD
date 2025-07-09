import { getProductById } from '@/services/productService';

type Props = {
    params: { id: string }
}

export default async function ProductDetailPage({ params }: Props) {
    const product = await getProductById(params.id);

    return (
        <div className="p-8">
            <h1 className="text-3xl mb-4">{product.nom}</h1>
            <p>{product.description}</p>
            <p>Prix : {product.prix} €</p>
            <p>Catégorie : {product.categorie}</p>
            <p>Quantité : {product.quantite}</p>
        </div>
    );
}

