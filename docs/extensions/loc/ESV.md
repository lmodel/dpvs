---
search:
  boost: 10.0
---

# Class: ESV 


_Concept representing region Province of Valencia in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-V](https://w3id.org/lmodel/dpv/loc/ES-V)





```mermaid
 classDiagram
    class ESV
    click ESV href "../ESV/"
      ES <|-- ESV
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-V](https://w3id.org/lmodel/dpv/loc/ES-V) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-V
* Province of Valencia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-V |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-V |
| native | loc:ESV |
| exact | dpv_loc:ES-V, dpv_loc_owl:ES-V |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-V
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Valencia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-V
- Province of Valencia
exact_mappings:
- dpv_loc:ES-V
- dpv_loc_owl:ES-V
is_a: ES
class_uri: loc:ES-V

```
</details>

### Induced

<details>
```yaml
name: ESV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-V
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Valencia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-V
- Province of Valencia
exact_mappings:
- dpv_loc:ES-V
- dpv_loc_owl:ES-V
is_a: ES
class_uri: loc:ES-V

```
</details></div>