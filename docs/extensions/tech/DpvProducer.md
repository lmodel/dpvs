---
search:
  boost: 10.0
---

# Class: DpvProducer 


_Actor that produces Technology_



<div data-search-exclude markdown="1">



URI: [tech:Producer](https://w3id.org/lmodel/dpv/tech/Producer)





```mermaid
 classDiagram
    class DpvProducer
    click DpvProducer href "../DpvProducer/"
      Actor <|-- DpvProducer
        click Actor href "../Actor/"
      

      DpvProducer <|-- Developer
        click Developer href "../Developer/"
      

      
```





## Inheritance
* [Actor](Actor.md)
    * **DpvProducer**
        * [Developer](Developer.md) [ [Actor](Actor.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Producer](https://w3id.org/lmodel/dpv/tech/Producer) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Producer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Producer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Producer |
| native | tech:DpvProducer |
| exact | dpv_tech:Producer, dpv_tech_owl:Producer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvProducer
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Producer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that produces Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Producer
exact_mappings:
- dpv_tech:Producer
- dpv_tech_owl:Producer
is_a: Actor
class_uri: tech:Producer

```
</details>

### Induced

<details>
```yaml
name: DpvProducer
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Producer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that produces Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Producer
exact_mappings:
- dpv_tech:Producer
- dpv_tech_owl:Producer
is_a: Actor
class_uri: tech:Producer

```
</details></div>