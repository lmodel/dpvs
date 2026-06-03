---
search:
  boost: 10.0
---

# Class: SmartphoneApplication 


_A computing or digital program on a smartphone device_



<div data-search-exclude markdown="1">



URI: [tech:SmartphoneApplication](https://w3id.org/lmodel/dpv/tech/SmartphoneApplication)





```mermaid
 classDiagram
    class SmartphoneApplication
    click SmartphoneApplication href "../SmartphoneApplication/"
      DpvApplication <|-- SmartphoneApplication
        click DpvApplication href "../DpvApplication/"
      
      
```





## Inheritance
* **SmartphoneApplication** [ [DpvApplication](DpvApplication.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:SmartphoneApplication](https://w3id.org/lmodel/dpv/tech/SmartphoneApplication) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Smartphone Application




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#SmartphoneApplication |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:SmartphoneApplication |
| native | tech:SmartphoneApplication |
| exact | dpv_tech:SmartphoneApplication, dpv_tech_owl:SmartphoneApplication |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SmartphoneApplication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SmartphoneApplication
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A computing or digital program on a smartphone device
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Smartphone Application
exact_mappings:
- dpv_tech:SmartphoneApplication
- dpv_tech_owl:SmartphoneApplication
mixins:
- DpvApplication
class_uri: tech:SmartphoneApplication

```
</details>

### Induced

<details>
```yaml
name: SmartphoneApplication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#SmartphoneApplication
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A computing or digital program on a smartphone device
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Smartphone Application
exact_mappings:
- dpv_tech:SmartphoneApplication
- dpv_tech_owl:SmartphoneApplication
mixins:
- DpvApplication
class_uri: tech:SmartphoneApplication

```
</details></div>