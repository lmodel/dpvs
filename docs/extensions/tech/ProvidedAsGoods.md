---
search:
  boost: 10.0
---

# Class: ProvidedAsGoods 


_Technology provided or used as goods_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsGoods](https://w3id.org/lmodel/dpv/tech/ProvidedAsGoods)





```mermaid
 classDiagram
    class ProvidedAsGoods
    click ProvidedAsGoods href "../ProvidedAsGoods/"
      ProvisionMethod <|-- ProvidedAsGoods
        click ProvisionMethod href "../ProvisionMethod/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * **ProvidedAsGoods**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsGoods](https://w3id.org/lmodel/dpv/tech/ProvidedAsGoods) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as GoodsProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsGoods |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsGoods |
| native | tech:ProvidedAsGoods |
| exact | dpv_tech:ProvidedAsGoods, dpv_tech_owl:ProvidedAsGoods |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsGoods
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsGoods
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided or used as goods
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as GoodsProvision
exact_mappings:
- dpv_tech:ProvidedAsGoods
- dpv_tech_owl:ProvidedAsGoods
is_a: ProvisionMethod
class_uri: tech:ProvidedAsGoods

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsGoods
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsGoods
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided or used as goods
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as GoodsProvision
exact_mappings:
- dpv_tech:ProvidedAsGoods
- dpv_tech_owl:ProvidedAsGoods
is_a: ProvisionMethod
class_uri: tech:ProvidedAsGoods

```
</details></div>