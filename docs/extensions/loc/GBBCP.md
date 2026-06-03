---
search:
  boost: 10.0
---

# Class: GBBCP 


_Concept representing region Bournemouth, Christchurch and Poole in_

_country United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-BCP](https://w3id.org/lmodel/dpv/loc/GB-BCP)





```mermaid
 classDiagram
    class GBBCP
    click GBBCP href "../GBBCP/"
      GB <|-- GBBCP
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBBCP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-BCP](https://w3id.org/lmodel/dpv/loc/GB-BCP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-BCP
* Bournemouth, Christchurch and Poole




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-BCP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-BCP |
| native | loc:GBBCP |
| exact | dpv_loc:GB-BCP, dpv_loc_owl:GB-BCP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBBCP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BCP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Bournemouth, Christchurch and Poole in

  country United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BCP
- Bournemouth, Christchurch and Poole
exact_mappings:
- dpv_loc:GB-BCP
- dpv_loc_owl:GB-BCP
is_a: GB
class_uri: loc:GB-BCP

```
</details>

### Induced

<details>
```yaml
name: GBBCP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BCP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Bournemouth, Christchurch and Poole in

  country United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BCP
- Bournemouth, Christchurch and Poole
exact_mappings:
- dpv_loc:GB-BCP
- dpv_loc_owl:GB-BCP
is_a: GB
class_uri: loc:GB-BCP

```
</details></div>