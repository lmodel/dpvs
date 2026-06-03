---
search:
  boost: 10.0
---

# Class: ProvidedAsProduct 


_Technology provided as a product_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsProduct](https://w3id.org/lmodel/dpv/tech/ProvidedAsProduct)





```mermaid
 classDiagram
    class ProvidedAsProduct
    click ProvidedAsProduct href "../ProvidedAsProduct/"
      ProvisionMethod <|-- ProvidedAsProduct
        click ProvisionMethod href "../ProvisionMethod/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * **ProvidedAsProduct**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsProduct](https://w3id.org/lmodel/dpv/tech/ProvidedAsProduct) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as ProductProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsProduct |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsProduct |
| native | tech:ProvidedAsProduct |
| exact | dpv_tech:ProvidedAsProduct, dpv_tech_owl:ProvidedAsProduct |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsProduct
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsProduct
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a product
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as ProductProvision
exact_mappings:
- dpv_tech:ProvidedAsProduct
- dpv_tech_owl:ProvidedAsProduct
is_a: ProvisionMethod
class_uri: tech:ProvidedAsProduct

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsProduct
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsProduct
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a product
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as ProductProvision
exact_mappings:
- dpv_tech:ProvidedAsProduct
- dpv_tech_owl:ProvidedAsProduct
is_a: ProvisionMethod
class_uri: tech:ProvidedAsProduct

```
</details></div>