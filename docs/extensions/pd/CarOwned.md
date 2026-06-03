---
search:
  boost: 10.0
---

# Class: CarOwned 


_Information about cars ownership and ownership history_



<div data-search-exclude markdown="1">



URI: [pd:CarOwned](https://w3id.org/lmodel/dpv/pd/CarOwned)





```mermaid
 classDiagram
    class CarOwned
    click CarOwned href "../CarOwned/"
      Ownership <|-- CarOwned
        click Ownership href "../Ownership/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Ownership](Ownership.md)
        * **CarOwned**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CarOwned](https://w3id.org/lmodel/dpv/pd/CarOwned) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Car Owned




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CarOwned |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CarOwned |
| native | pd:CarOwned |
| exact | dpv_pd:CarOwned, dpv_pd_owl:CarOwned |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CarOwned
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CarOwned
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about cars ownership and ownership history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Car Owned
exact_mappings:
- dpv_pd:CarOwned
- dpv_pd_owl:CarOwned
is_a: Ownership
class_uri: pd:CarOwned

```
</details>

### Induced

<details>
```yaml
name: CarOwned
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CarOwned
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about cars ownership and ownership history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Car Owned
exact_mappings:
- dpv_pd:CarOwned
- dpv_pd_owl:CarOwned
is_a: Ownership
class_uri: pd:CarOwned

```
</details></div>