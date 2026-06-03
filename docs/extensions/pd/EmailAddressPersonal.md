---
search:
  boost: 10.0
---

# Class: EmailAddressPersonal 


_Information about email address used in personal capacity_



<div data-search-exclude markdown="1">



URI: [pd:EmailAddressPersonal](https://w3id.org/lmodel/dpv/pd/EmailAddressPersonal)





```mermaid
 classDiagram
    class EmailAddressPersonal
    click EmailAddressPersonal href "../EmailAddressPersonal/"
      EmailAddress <|-- EmailAddressPersonal
        click EmailAddress href "../EmailAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [EmailAddress](EmailAddress.md)
            * **EmailAddressPersonal**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EmailAddressPersonal](https://w3id.org/lmodel/dpv/pd/EmailAddressPersonal) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Email Address Personal




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EmailAddressPersonal |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EmailAddressPersonal |
| native | pd:EmailAddressPersonal |
| exact | dpv_pd:EmailAddressPersonal, dpv_pd_owl:EmailAddressPersonal |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EmailAddressPersonal
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmailAddressPersonal
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about email address used in personal capacity
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Email Address Personal
exact_mappings:
- dpv_pd:EmailAddressPersonal
- dpv_pd_owl:EmailAddressPersonal
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: EmailAddress
class_uri: pd:EmailAddressPersonal

```
</details>

### Induced

<details>
```yaml
name: EmailAddressPersonal
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmailAddressPersonal
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about email address used in personal capacity
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Email Address Personal
exact_mappings:
- dpv_pd:EmailAddressPersonal
- dpv_pd_owl:EmailAddressPersonal
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: EmailAddress
class_uri: pd:EmailAddressPersonal

```
</details></div>