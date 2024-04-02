import { Component, OnInit } from '@angular/core';
import { Product, products } from '../products';
import { Category, categories } from '../categories';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  category : Category | undefined;
  product : Product | undefined;
  products = products;

  like(product: Product): void {
    product.likeCount++;
  }
  constructor(
    private _activatedRoute: ActivatedRoute
  ) {
    this._activatedRoute.paramMap.subscribe(params => {
      this.ngOnInit();
    });
  }
  ngOnInit() {
    this.reloadCategory();
  }

  reloadCategory() {
    const routeParams = this._activatedRoute.snapshot.paramMap;
    const productCategoryFromRoute = String(routeParams.get('categories'));
    // Find the product that correspond with the id provided in route.
    this.category = categories.find(category => category.category === productCategoryFromRoute);
  }

  deleteProduct(product: Product): void {
    const index = products.findIndex(p => p.id === product.id);
    if (index !== -1) {
      products.splice(index, 1);
    }
  }
}



