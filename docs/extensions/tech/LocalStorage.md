---
search:
  boost: 10.0
---

# Class: LocalStorage 


_Storage that is local (e.g. on device)_



<div data-search-exclude markdown="1">



URI: [tech:LocalStorage](https://w3id.org/lmodel/dpv/tech/LocalStorage)





```mermaid
 classDiagram
    class LocalStorage
    click LocalStorage href "../LocalStorage/"
      DataStorage <|-- LocalStorage
        click DataStorage href "../DataStorage/"
      

      LocalStorage <|-- Cookie
        click Cookie href "../Cookie/"
      

      
```





## Inheritance
* **LocalStorage** [ [DataStorage](DataStorage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:LocalStorage](https://w3id.org/lmodel/dpv/tech/LocalStorage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Local Storage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#LocalStorage |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:LocalStorage |
| native | tech:LocalStorage |
| exact | dpv_tech:LocalStorage, dpv_tech_owl:LocalStorage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LocalStorage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#LocalStorage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Storage that is local (e.g. on device)
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Local Storage
exact_mappings:
- dpv_tech:LocalStorage
- dpv_tech_owl:LocalStorage
mixins:
- DataStorage
class_uri: tech:LocalStorage

```
</details>

### Induced

<details>
```yaml
name: LocalStorage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#LocalStorage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Storage that is local (e.g. on device)
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Local Storage
exact_mappings:
- dpv_tech:LocalStorage
- dpv_tech_owl:LocalStorage
mixins:
- DataStorage
class_uri: tech:LocalStorage

```
</details></div>