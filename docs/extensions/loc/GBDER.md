---
search:
  boost: 10.0
---

# Class: GBDER 


_Concept representing region Derby in country United Kingdom of Great_

_Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-DER](https://w3id.org/lmodel/dpv/loc/GB-DER)





```mermaid
 classDiagram
    class GBDER
    click GBDER href "../GBDER/"
      GB <|-- GBDER
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBDER**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-DER](https://w3id.org/lmodel/dpv/loc/GB-DER) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-DER
* Derby




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-DER |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-DER |
| native | loc:GBDER |
| exact | dpv_loc:GB-DER, dpv_loc_owl:GB-DER |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBDER
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DER
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Derby in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DER
- Derby
exact_mappings:
- dpv_loc:GB-DER
- dpv_loc_owl:GB-DER
is_a: GB
class_uri: loc:GB-DER

```
</details>

### Induced

<details>
```yaml
name: GBDER
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-DER
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Derby in country United Kingdom of Great

  Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-DER
- Derby
exact_mappings:
- dpv_loc:GB-DER
- dpv_loc_owl:GB-DER
is_a: GB
class_uri: loc:GB-DER

```
</details></div>