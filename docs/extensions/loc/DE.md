---
search:
  boost: 10.0
---

# Class: DE 


_Concept representing Country of Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE](https://w3id.org/lmodel/dpv/loc/DE)





```mermaid
 classDiagram
    class DE
    click DE href "../DE/"
      EEA30 <|-- DE
        click EEA30 href "../EEA30/"
      EEA31 <|-- DE
        click EEA31 href "../EEA31/"
      EU <|-- DE
        click EU href "../EU/"
      EU27 <|-- DE
        click EU27 href "../EU27/"
      EU28 <|-- DE
        click EU28 href "../EU28/"
      EEA <|-- DE
        click EEA href "../EEA/"
      

      DE <|-- DEBB
        click DEBB href "../DEBB/"
      DE <|-- DEBE
        click DEBE href "../DEBE/"
      DE <|-- DEBW
        click DEBW href "../DEBW/"
      DE <|-- DEBY
        click DEBY href "../DEBY/"
      DE <|-- DEHB
        click DEHB href "../DEHB/"
      DE <|-- DEHE
        click DEHE href "../DEHE/"
      DE <|-- DEHH
        click DEHH href "../DEHH/"
      DE <|-- DEMV
        click DEMV href "../DEMV/"
      DE <|-- DENI
        click DENI href "../DENI/"
      DE <|-- DENW
        click DENW href "../DENW/"
      DE <|-- DERP
        click DERP href "../DERP/"
      DE <|-- DESH
        click DESH href "../DESH/"
      DE <|-- DESL
        click DESL href "../DESL/"
      DE <|-- DESN
        click DESN href "../DESN/"
      DE <|-- DEST
        click DEST href "../DEST/"
      DE <|-- DETH
        click DETH href "../DETH/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **DE** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [DEBB](DEBB.md)
        * [DEBE](DEBE.md)
        * [DEBW](DEBW.md)
        * [DEBY](DEBY.md)
        * [DEHB](DEHB.md)
        * [DEHE](DEHE.md)
        * [DEHH](DEHH.md)
        * [DEMV](DEMV.md)
        * [DENI](DENI.md)
        * [DENW](DENW.md)
        * [DERP](DERP.md)
        * [DESH](DESH.md)
        * [DESL](DESL.md)
        * [DESN](DESN.md)
        * [DEST](DEST.md)
        * [DETH](DETH.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE](https://w3id.org/lmodel/dpv/loc/DE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Germany




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE |
| native | loc:DE |
| exact | dpv_loc:DE, dpv_loc_owl:DE, iso3166:DE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Germany
exact_mappings:
- dpv_loc:DE
- dpv_loc_owl:DE
- iso3166:DE
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:DE

```
</details>

### Induced

<details>
```yaml
name: DE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Germany
exact_mappings:
- dpv_loc:DE
- dpv_loc_owl:DE
- iso3166:DE
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:DE

```
</details></div>