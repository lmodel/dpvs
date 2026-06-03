---
search:
  boost: 10.0
---

# Class: EmailAddress 


_Information about email address_



<div data-search-exclude markdown="1">



URI: [pd:EmailAddress](https://w3id.org/lmodel/dpv/pd/EmailAddress)





```mermaid
 classDiagram
    class EmailAddress
    click EmailAddress href "../EmailAddress/"
      Contact <|-- EmailAddress
        click Contact href "../Contact/"
      

      EmailAddress <|-- EmailAddressPersonal
        click EmailAddressPersonal href "../EmailAddressPersonal/"
      EmailAddress <|-- EmailAddressWork
        click EmailAddressWork href "../EmailAddressWork/"
      

      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * **EmailAddress**
            * [EmailAddressPersonal](EmailAddressPersonal.md)
            * [EmailAddressWork](EmailAddressWork.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EmailAddress](https://w3id.org/lmodel/dpv/pd/EmailAddress) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Email Address




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EmailAddress |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EmailAddress |
| native | pd:EmailAddress |
| exact | dpv_pd:EmailAddress, dpv_pd_owl:EmailAddress |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EmailAddress
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmailAddress
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about email address
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Email Address
exact_mappings:
- dpv_pd:EmailAddress
- dpv_pd_owl:EmailAddress
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Contact
class_uri: pd:EmailAddress

```
</details>

### Induced

<details>
```yaml
name: EmailAddress
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmailAddress
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about email address
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Email Address
exact_mappings:
- dpv_pd:EmailAddress
- dpv_pd_owl:EmailAddress
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Contact
class_uri: pd:EmailAddress

```
</details></div>