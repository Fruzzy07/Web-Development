export interface Product {
  id: number;
  name: string;
  image: string;
  images: string[];
  price: number;
  description: string;
  rating: number;
  link: string;
}

export const products = [
  {
    id: 1,
    name: 'Electric kettle BEREKE BR-810 grey',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/h08/hde/80282292781086.jpg?format=gallery-large',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/h08/hde/80282292781086.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h08/hde/80282292781086.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h08/hde/80282292781086.jpg?format=gallery-medium',
    ],
    price: 1748,
    description:
      'Descaling filter: No, Type:electric kettle, volume: 2.0L, Power: 1500.0W, Case material: Stainless steel, Color: Grey',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/elektrochainik-bereke-br-810-seryi-109981423/?c=750000000',
  },

  {
    id: 2,
    name: 'Kitchen scales Generic SF-400',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/h47/ha1/64094073815070.jpg?format=gallery-medium',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/hcf/ha8/64094074798110.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h5a/h8f/64094077124638.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h47/ha1/64094073815070.jpg?format=gallery-medium',
    ],
    price: 799,
    description:
      'Type: electronic, weighing limit: 10.0kg, Measurement accuracy: 1.0g, Calorie counter: Yes,Color: White',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/generic-sf-400-102531445/?c=750000000',
  },

  {
    id: 3,
    name: 'Blender SM-7700 silver',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/h78/he6/81315957440542.png?format=gallery-large',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/h78/he6/81315957440542.png?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h78/he6/81315957440542.png?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h78/he6/81315957440542.png?format=gallery-medium',
    ],
    price: 8749,
    description:
      'Type: Stationary, Power: 1000.0W, Control: Mechanical, Number of speeds: 3, Chopper: Yes, Color: Silver',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/sm-7700-serebristyi-110902818/?c=750000000',
  },

  {
    id: 4,
    name: 'Vacuum cleaner Deerma DX700 white',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/hdb/h2f/63803859566622.jpg?format=gallery-medium',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/h20/he1/63803865792542.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/had/h34/63803868741662.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h2e/h83/63803872280606.jpg?format=gallery-medium',
    ],
    price: 19147,
    description:
      'Type: vertical, cleaning: dry, Dust collector type: cyclone filter, Power consumption: 600.0W, Power source: mains, color: White',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/deerma-dx700-belyi-3701383/?c=750000000',
  },

  {
    id: 5,
    name: 'Maxmoll H2O Humidifier-300 white',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/hd0/hc4/64156819783710.jpg?format=gallery-medium',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/hf6/h4e/64156857008158.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h2f/hfc/64156859138078.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hfc/h94/64156861366302.jpg?format=gallery-medium',
    ],
    price: 1448,
    description:
      'purpose of the device: humidification, of the serviced area: 10.0 sq.m, control: mechanical, humidifier type: ultrasonic, color: white',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/uvlazhnitel-vozduha-maxmoll-h2o-humid-300-belyi-102027263/?c=750000000',
  },

  {
    id: 6,
    name: 'Proliss Pro-808 Waffle Iron black',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/h49/h36/64432195403806.jpg?format=gallery-medium',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/h49/h36/64432195403806.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h49/h36/64432195403806.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h49/h36/64432195403806.jpg?format=gallery-medium',
    ],
    price: 3807,
    description:
      'Body material: Metal/Plastic, Type: Waffle, iron Number of servings: 2, Non-stick coating: Yes, Color: Black',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/vafel-nitsa-proliss-pro-808-chernyi-105935489/?c=750000000',
  },

  {
    id: 7,
    name: 'Immersion Blender Slaouwo HB-2075 white',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/hfe/ha1/67141660606494.jpg?format=gallery-medium',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/hfe/ha1/67141660606494.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hfe/ha1/67141660606494.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hfe/ha1/67141660606494.jpg?format=gallery-medium',
    ],
    price: 7398,
    description:
      'Type: Submersible, Power: 800.0W, Control: Electronic, Number of speeds: 6, Chopper: Yes, Color: White',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/pogruzhnoi-slaouwo-hb-2075-belyi-108151055/?c=750000000',
  },

  {
    id: 8,
    name: 'Samsung VCC4520S3R/XEV Vacuum Cleaner Red',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/heb/h01/63769265045534.jpg?format=gallery-medium',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/h86/h14/63769265766430.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h29/h78/63769266094110.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h45/hda/63769266946078.jpg?format=gallery-medium',
    ],
    price: 30295,
    description:
      'Type: traditional, cleaning: dry, Dust collector type: Cyclone filter, Power consumption: 1600.0W, Power source: Mains, Color: Red',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/samsung-vcc4520s3r-xev-krasnyi-3700926/?c=750000000',
  },

  {
    id: 9,
    name: 'Braun MQ 5235 blender white, grey',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/hee/h94/63861302263838.jpg?format=gallery-medium',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/h29/h4f/63861305016350.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hee/h94/63861302263838.jpg?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/hee/h94/63861302263838.jpg?format=gallery-medium',
    ],
    price: 12479,
    description:
      'Type: submersible, power: 1000.0 W, Control: mechanical, number of speeds: 21, Chopper: Yes, Color: white ,grey',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/braun-mq-5235-belyi-seryi-100435308/?c=750000000',
  },

  {
    id: 10,
    name: 'Vacuum cleaner Deerma DX700S grey',
    image:
      'https://resources.cdn-kaspi.kz/img/m/p/hd7/h74/63950404878366.jpg?format=gallery-large',
    images: [
      'https://resources.cdn-kaspi.kz/img/m/p/hb9/h89/63950413692958.jpg?format=gallery-large',
      'https://resources.cdn-kaspi.kz/img/m/p/he2/h73/80496921542686.png?format=gallery-medium',
      'https://resources.cdn-kaspi.kz/img/m/p/h71/hc5/63950415855646.jpg?format=gallery-medium',
    ],
    price: 18493,
    description:
      'Type: vertical, cleaning: dry, Dust collector type: cyclone filter, Power consumption: 600.0W, Power supply: mains, color: grey',
    rating: 5,
    link: 'https://kaspi.kz/shop/p/deerma-dx700s-seryi-100680527/?c=750000000',
  },
];

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
